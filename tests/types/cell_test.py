from quarto_lib.types.cell import Cell


class TestCell:
    def test_row(self):
        assert Cell.C1.row == 3
        assert Cell.C2.row == 2
        assert Cell.C3.row == 1
        assert Cell.C4.row == 0

    def test_col(self):
        assert Cell.C1.col == 2
        assert Cell.C2.col == 2
        assert Cell.C3.col == 2
        assert Cell.C4.col == 2
