import pytest
import selenium
##############################################################################################
"""
    Testing methods and classes for functions unit tests
"""
##############################################################################################
# Import all test files
import core
import core.mytestunity.system_file
import core.web_core
##############################################################################################



if __name__ == "__main__":
    # Run all tests available
    
    pytest.main(["-v", __file__])