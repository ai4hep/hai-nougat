import sys
from utils import crawl, process, crawl_and_process
from parse_parameter import parse_arg

def main():
    parameters = parse_arg(sys.argv[1:])    
    if parameters.crawl and not parameters.process:
        crawl(parameters)
    elif parameters.process and not parameters.crawl:
        process(parameters)
    elif parameters.process and parameters.crawl:
        crawl_and_process(parameters)
    elif not parameters.crawl and not parameters.process:
        print('You need to specify at least one of crawl and process to be True')
    return 

if __name__ == '__main__':
    main()
    