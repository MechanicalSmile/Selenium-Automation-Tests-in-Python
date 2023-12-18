import concurrent.futures
from tests import *


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(sign_up_for_newsletter), executor.submit(add_remove_elements), executor.submit(basic_authorization), executor.submit(find_broken_images)]

        # Wait for both scripts to finish
        concurrent.futures.wait(futures)

        # Check the results and print success messages
        for future, test_name in zip(futures, ["Test1", "Test2", "Test3", "Test4"]):
            try:
                result = future.result()
                assert result is True
                print(f"{test_name} is successful with no errors")
            except AssertionError as e:
                if str(e):
                    print(f"{test_name} failed. Error Details: {str(e)}")
                else:
                    print(f"{test_name} failed: {result}")