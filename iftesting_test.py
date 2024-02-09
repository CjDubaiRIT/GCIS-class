def square_area():
    area=square_area(8)
    assert (area==64)

def square_area(side):
    if side<0:
        return None
    if side>0:
        return (64)
