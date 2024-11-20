def test_data_generator():
    for i in range(1, 6):
        yield i

for data in test_data_generator():
    print(data)