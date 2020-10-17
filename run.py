from code import Scheduler, PageFetcher
import time
import threading

if __name__ == "__main__":
    start = time.time()

    # Criação dos elementos da coleta: Scheduler e fetcher
    scheduler = Scheduler(str_usr_agent="Group2bot",
                                int_page_limit=14,
                                int_depth_limit=6,
                                arr_urls_seeds=[])
    fetcher = PageFetcher(scheduler)

    # Criação da fila e coleta
    fetcher.insertURLs()
    fetcher.run()

    # Separação em threads
    thread1 = threading.Thread(target = fetcher.run())
    thread2 = threading.Thread(target = fetcher.run())
    thread3 = threading.Thread(target = fetcher.run())

    end = time.time()
    print('Tempo de execucao: {}'.format(end-start))
   
