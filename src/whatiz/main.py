#!/usr/bin/env python3
import sys
import warnings
import logging
from ddgs import DDGS

# Suppress DDGS warnings
warnings.filterwarnings("ignore", category=UserWarning)
logging.getLogger("duckduckgo_search").setLevel(logging.ERROR)


def main():

  try:
    if len(sys.argv) > 1:
      with DDGS() as ddgs:
        result = ddgs.text(sys.argv[1], max_results=1)
        body:str = result[0].get('body')
        main_content, sep, after = body.partition('.')
        print("\n\n"+main_content+"...\n\n")
    
    else:
      print("Please provide a parameter.")
  except ConnectionError or ddgs.exceptions.DDGSException as e:
    print("Please have an internet connection...")


if __name__ == "__main__":
  main()