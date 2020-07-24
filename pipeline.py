import logging
logging.basicConfig(level=logging.INFO)
import subprocess
import datetime

logger = logging.getLogger(__name__)
news_sites_uids = ['MontevideoPortal']

def main():
    _extract()
    _transform()
    _load()


def _extract():
    logger.info('Starting extract process')
    for news_site_uid in news_sites_uids:
        subprocess.run(['env/Scripts/python','main.py', news_site_uid] , cwd='./extract')
        subprocess.run(['move','{}_articles.csv'.format(news_site_uid), '../transform'],cwd='./extract', shell=True)


def _transform():
    logger.info('Starting transform process')
    for news_site_uid in news_sites_uids:
        dirty_data_filename = '{}_articles.csv'.format(news_site_uid)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(['env/Scripts/python', 'main.py', dirty_data_filename], cwd='./transform')
        subprocess.run(['del', dirty_data_filename], cwd='./transform', shell=True)
        subprocess.run(['move', clean_data_filename, '../load'], cwd='./transform' , shell=True)


def _load():
    logger.info('Starting loading process')
    for news_site_uid in news_sites_uids:
        clean_data_filename = 'clean_{}_articles.csv'.format(news_site_uid)
        subprocess.run(['env/Scripts/python', 'main.py', clean_data_filename], cwd='./load')
        subprocess.run(['del', clean_data_filename], cwd='./load' , shell=True)


if __name__ == '__main__':
    main()
