class Pool:
    '''
    Whatever pool
    '''

    def __init__(self, items):
        self._items = items

    def __len__(self):
        return self._items


if __name__ == '__main__':
    p = Pool(15)
    print(len(p))