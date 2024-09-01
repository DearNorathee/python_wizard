from python_wizard.year_month import *
def test_create_year_month_list():
    actual01 = create_year_month_list(2020, 2021, "list")
    actual02 = create_year_month_list(2020, 2021, "np_array")
    
    expect01 = ['202001', '202002', '202003', '202004', '202005', '202006', '202007', '202008', '202009', '202010', '202011', '202012', '202101', '202102', '202103', '202104', '202105', '202106', '202107', '202108', '202109', '202110', '202111', '202112']
    expect02 = np.array(expect01)
    assert isinstance(actual01,list)
    
    assert np.array_equal(actual02 ,expect02)
    assert isinstance(actual02,np.ndarray)

test_create_year_month_list()

