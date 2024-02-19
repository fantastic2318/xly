import pytest


class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert 'x' in x

    @pytest.mark.parametrize('x, y', [(1, 1), (7, 8)])
    def test_three(self, x, y):
        print(f'Nodeidsis::test_three::{x}=={y}')
        assert x == y


if __name__ == '__main__':
    pytest.main(['-v', '--reruns=1','test_class_sample.py'])