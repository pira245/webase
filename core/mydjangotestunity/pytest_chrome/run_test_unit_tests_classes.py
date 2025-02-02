import pytest
import selenium
##############################################################################################
"""
    Testing methods and classes for classes unit tests
"""
##############################################################################################
# Import all test files
import core
import core.mydjangotestunity.system_file
import core.web_core
##############################################################################################



if __name__ == "__main__":
    # Run all tests available
    
    pytest.main(["-v", __file__])