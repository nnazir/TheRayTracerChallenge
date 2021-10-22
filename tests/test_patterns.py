from trtc.matrix import Matrix
import trtc.tuple
from trtc.tuple import WHITE, BLACK, point
from trtc.pattern import StripePattern
from trtc.sphere import Sphere


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


def test_stripes_with_object_transformation():
    '''  Stripes with an object transformation  '''
    obj = Sphere()
    obj.transform = Matrix.scaling(2, 2, 2)
    pattern = StripePattern(WHITE, BLACK)
    c = pattern.stripe_at_object(obj, point(1.5, 0, 0))
    assert c == WHITE


def test_stripes_with_pattern_transformation():
    '''  Stripes with a pattern transformation  '''
    obj = Sphere()
    pattern = StripePattern(WHITE, BLACK)
    pattern.transform = Matrix.scaling(2, 2, 2)
    c = pattern.stripe_at_object(obj, point(1.5, 0, 0))
    assert c == WHITE


def test_stripes_with_object_and_pattern_transformation():
    '''  Stripes with both an object and a a pattern transformation  '''
    obj = Sphere()
    obj.transform = Matrix.scaling(2, 2, 2)
    pattern = StripePattern(WHITE, BLACK)
    pattern.transform = Matrix.translation(0.5, 0, 0)
    c = pattern.stripe_at_object(obj, point(2.5, 0, 0))
    assert c == WHITE
