import trtc.tuple
from trtc.tuple import WHITE, BLACK, point
from trtc.pattern import StripePattern


def test_create_stripe_pattern():
    '''  Creating a stripe pattern  '''
    pattern = StripePattern(trtc.tuple.WHITE, trtc.tuple.BLACK)
    assert pattern.a == WHITE
    assert pattern.b == BLACK


def test_stripe_pattern_constant_y():
    '''  A stripe pattern is constant in y  '''
    pattern = StripePattern(WHITE, BLACK)
    assert pattern.stripe_at(point(0, 0, 0)) == WHITE
    assert pattern.stripe_at(point(0, 1, 0)) == WHITE
    assert pattern.stripe_at(point(0, 2, 0)) == WHITE


def test_stripe_pattern_constant_z():
    '''  A stript pattern is constant in z  '''
    pattern = StripePattern(WHITE, BLACK)
    assert pattern.stripe_at(point(0, 0, 0)) == WHITE
    assert pattern.stripe_at(point(0, 0, 1)) == WHITE
    assert pattern.stripe_at(point(0, 0, 2)) == WHITE


def test_stripe_pattern_alternate_x():
    '''  A stripe pattern alternates in x  '''
    pattern = StripePattern(WHITE, BLACK)
    assert pattern.stripe_at(point(0, 0, 0)) == WHITE
    assert pattern.stripe_at(point(0.9, 0, 0)) == WHITE
    assert pattern.stripe_at(point(1, 0, 0)) == BLACK
    assert pattern.stripe_at(point(-0.1, 0, 0)) == BLACK
    assert pattern.stripe_at(point(-1, 0, 0)) == BLACK
    assert pattern.stripe_at(point(-1.1, 0, 0)) == WHITE
