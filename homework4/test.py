import unittest

from chess_fen import *
class TestChessException(unittest.TestCase):
    """Test the ChessException class."""
    def test_existence(self):
        """Sanity test for the ChessException class."""
        exception = ChessException('Paul Morphy')
class TestChessScore(unittest.TestCase):
    """Test the ChessScore class."""
    def test_simple_init(self):
        """Sanity test for the ChessScore class."""
        score = ChessScore(['p'])
    def test_conversion_to_int(self):
        """Test __int__ method."""
        score = ChessScore(['r', 'b'])
        self.assertEqual(int(score), 8)
    def test_empty_input(self):
        """Test empty array of pieces."""
        score = ChessScore([])
        self.assertEqual(int(score), 0)
    def test_less_than_operator(self):
        """Test __lt__ method."""
        rock_score = ChessScore(['r'])
        queen_score = ChessScore(['q'])
        self.assertLess(rock_score, queen_score)
    def test_less_than_or_equal_operator(self):
        """Test __le__ method."""
        rock_score = ChessScore(['r'])
        queen_score = ChessScore(['q'])
        self.assertLessEqual(rock_score, queen_score)
    def test_equal_operator(self):
        """Test __eq__ method."""
        king1 = ChessScore(['k'])
        king2 = ChessScore(['k'])
        self.assertEqual(king1, king2)
    def test_greater_than_or_equal_operator(self):
        """Test __ge__ method."""
        queen_score = ChessScore(['q'])
        rock_score = ChessScore(['r'])
        self.assertGreaterEqual(queen_score, rock_score)
    def test_greater_than_operator(self):
        """Test __gt__ method."""
        queen_score = ChessScore(['q'])
        rock_score = ChessScore(['r'])
        self.assertGreater(queen_score, rock_score)
    def test_not_equal_operator(self):
        """Test __ne__ method."""
        queen_score = ChessScore(['q'])
        rock_score = ChessScore(['r'])
        self.assertNotEqual(queen_score, rock_score)
    def test_addition_operator(self):
        """Test __add__ method."""
        score1 = ChessScore(['q', 'p'])
        score2 = ChessScore(['r', 'n'])
        self.assertEqual(score1+score2, 18)
    def test_subtraction_operator(self):
        """Test __sub__ method."""
        score1 = ChessScore(['q', 'p'])
        score2 = ChessScore(['r', 'n'])
        self.assertEqual(score1-score2, 2)
class TestChessPosition(unittest.TestCase):
    """Test the ChessPosition class."""
    def test_simple_init(self):
        """Sanity test for the ChessPosition class."""
        init_pos = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        self.assertTrue(hasattr(init_pos, 'get_white_score'))
        self.assertTrue(hasattr(init_pos, 'get_black_score'))
        self.assertTrue(hasattr(init_pos, 'white_is_winning'))
        self.assertTrue(hasattr(init_pos, 'black_is_winning'))
        self.assertTrue(hasattr(init_pos, 'is_equal'))
    def test_missing_king(self):
        """Test for missing king."""
        with self.assertRaises(ChessException) as cm:
            ChessPosition('rnbq1bnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        exception = cm.exception
        self.assertEqual(exception._message, 'kings')
    def test_multiple_kings(self):
        """Test for more than one kings of same color."""
        with self.assertRaises(ChessException) as cm:
            ChessPosition('rnbqkbnr/pkpppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')

        exception = cm.exception
        self.assertEqual(exception._message, 'kings')
    def test_neighbor_kings_1(self):
        """Test for kings next to each other."""
        with self.assertRaises(ChessException) as cm:
            ChessPosition('rnbqkKnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQ1BNR')
        exception = cm.exception
        self.assertEqual(exception._message, 'kings')
    def test_neighbor_kings_2(self):
        """Test for kings diagonally next to each other."""
        with self.assertRaises(ChessException) as cm:
            ChessPosition('rnbqkbnr/pppppKpp/8/8/8/8/PPPPPPPP/RNBQ1BNR')
        exception = cm.exception
        self.assertEqual(exception._message, 'kings')
    def test_invalid_pawns_position_1(self):
        """Test for pawn on eight row."""
        with self.assertRaises(ChessException) as cm:
            ChessPosition('rnbpkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        exception = cm.exception
        self.assertEqual(exception._message, 'pawns')
    def test_invalid_pawns_position_2(self):
        """Test for pawn on first row."""
        with self.assertRaises(ChessException) as cm:
            ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBPKBNR')

        exception = cm.exception
        self.assertEqual(exception._message, 'pawns')

    def test_string_representation(self):
        """Test __str__ method."""
        self.assertEqual(str(ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')),
                         'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')

    def test_len_method(self):
        """Test __len__ method."""
        self.assertEqual(len(ChessPosition('4k3/8/3pp2/8/8/8/1P6/4K3')), 5)

    def test_index_operator(self):
        """Test __getitem__ method."""
        position = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        score = int(ChessScore(
            [position['A8'], position['B7'], position['E8'].lower()]))

        self.assertEqual(score, 10)
        self.assertEqual(position['C6'], None)

    def test_get_white_score(self):
        """Test for getting white score."""
        position = ChessPosition('4k3/8/8/8/8/8/PPPPPPPP/4K3')

        self.assertEqual(int(position.get_white_score()), 12)

    def test_get_black_score(self):
        """Test for getting black score."""
        position = ChessPosition('4k3/8/8/8/8/8/PPPPPPPP/4K3')

        self.assertEqual(int(position.get_black_score()), 4)

    def test_white_is_winning(self):
        """Test for white_is_winning method."""
        position = ChessPosition('4k3/8/8/8/8/8/PPPPPPPP/4K3')

        self.assertTrue(position.white_is_winning())

    def test_black_is_winning(self):
        """Test for black_is_winning method."""
        position = ChessPosition('4k3/pppppppp/8/8/8/8/8/4K3')

        self.assertTrue(position.black_is_winning())

    def test_is_equal(self):
        """Test for is_equal method."""
        position = ChessPosition('4k3/pppppppp/8/8/8/8/PPPPPPPP/4K3')
        self.assertTrue(position.is_equal())
if __name__ == '__main__':
    unittest.main()