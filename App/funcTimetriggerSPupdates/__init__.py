import logging
import azure.functions as func

# app = func.FunctionApp()

# @app.timer_trigger(schedule="0 * * * * *", arg_name="req", run_on_startup=False, use_monitor=False)
def main(req: func.TimerRequest) -> None:
    if req.past_due:
        logging.info('The timer is past due!')

    logging.info('Hello App !!!!, Python timer trigger function executed.')
