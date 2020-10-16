from code import Scheduler, PageFetcher

if __name__ == "__main__":
    scheduler = Scheduler(str_usr_agent="Group2bot",
                                int_page_limit=6,
                                int_depth_limit=3,
                                arr_urls_seeds=[])
    fetcher = PageFetcher(scheduler)
    values = fetcher.run()
