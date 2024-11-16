from apscheduler.schedulers.background import BackgroundScheduler

from mailing.utils import check_and_send_mailing


def start():
    """ Функция для реализации периодических задач """
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_and_send_mailing, 'interval', seconds=10)
    scheduler.start()
