import MetaTrader5 as mt5
from datetime import datetime

def connect_to_mt5():
    if not mt5.initialize():
        print("Inicialização falhou, erro:", mt5.last_error())
        mt5.shutdown()
    else:
        print("Conectado com sucesso ao MetaTrader 5.")

def altera_sl_tp(ativo, take_profit, stop_loss, desc="Alterando SL e TP"):
    request = {
        "action": mt5.TRADE_ACTION_SLTP,
        "symbol": ativo,
        "sl": float(stop_loss),
        "tp": float(take_profit),
        "magic": 994980,
        "comment": desc,
        "type_time": mt5.ORDER_TIME_DAY,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }

    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print(f"-- ALTERAÇÃO SL e TP ENVIADA: ATIVO: {ativo} \nSL: {stop_loss} \nTP: {take_profit}")
    else:
        print(f"!! FALHA NA ALTERAÇÃO, retcode: {result.retcode}")
        log_error(result)
        
    return result

def compra_mercado(ativo, take_profit, stop_loss, num_lots, desc="Compra a Mercado"):
    price = mt5.symbol_info_tick(ativo).ask
    deviation = 5
    
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": ativo,
        "volume": num_lots,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": stop_loss,
        "tp": take_profit,
        "deviation": deviation,
        "magic": 994980,
        "comment": desc,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print(f"Compra efetuada: {ativo} \nVolume: {num_lots} \nPreço: {price}")
    else:
        print(f"Falha na compra, retcode: {result.retcode}")
        log_error(result)
        
    return result

def cancela_ordem():
    order = mt5.orders_get()[0] if mt5.orders_get() else None
    if order:
        request_cancelar = {
            "action": mt5.TRADE_ACTION_REMOVE,
            "order": order.ticket,
        }
        
        result = mt5.order_send(request_cancelar)
        if result.retcode == mt5.TRADE_RETCODE_DONE:
            print("Ordem cancelada com sucesso.")
        else:
            print("Falha ao cancelar ordem, retcode:", result.retcode)
            log_error(result)
    else:
        print("Nenhuma ordem encontrada para cancelar.")
        
    return result if order else None

def log_error(result):
    result_dict = result._asdict()
    for field in result_dict:
        print(f"{field}: {result_dict[field]}")
        if field == "request":
            traderequest_dict = result_dict[field]._asdict()
            for tradereq_field in traderequest_dict:
                print(f"traderequest -> {tradereq_field}: {traderequest_dict[tradereq_field]}")

def posso_operar(inicio, limite):
    agora = datetime.now().strftime('%H:%M:%S')
    return inicio < agora < limite

def myround(x, base=0.5):
    return base * round(x/base)
