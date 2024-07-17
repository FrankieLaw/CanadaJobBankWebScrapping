'''
    paginationLimit - Use for testing to limit how many jobs to be loaded.
                    - Typical jobs available in some provinces contains 30,000+ jobs
                    - To save time testing the application, this setting will
                    - override the pagination calculation to a fixed number.

    paginationSize  - A fixed number how many pages is to be loaded or how many
                    - times is this application to "click" 'load more' button.
'''
Scrappy = {
    'debugMode'            : False,
    'paginationSize'       : 5
}

