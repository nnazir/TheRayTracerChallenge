from trtc.matrix import Matrix
import trtc.tuple
from trtc.tuple import WHITE, BLACK, color, point
from trtc.pattern import TestPattern, StripePattern, GradientPattern, RingPattern
from trtc.sphere import Sphere


def test_create_stripe_pattern():
    '''  Scenario: Creating a stripe pattern  '''
    pattern = StripePattern(WHITE, BLACK)
    assert pattern.color_a == WHITE
    assert pattern.color_b == BLACK


def test_stripe_pattern_constant_y():
    '''  Scenario: A stripe pattern is constant in y  '''
    pattern = StripePattern(WHITE, BLACK)
    assert pattern.pattern_at(point(0, 0, 0)) == WHITE
    assert pattern.pattern_at(point(0, 1, 0)) == WHITE
    assert pattern.pattern_at(point(0, 2, 0)) == WHITE


def test_stripe_pattern_constant_z():
    '''  Scenario: A stript pattern is constant in z  '''
    pattern = StripePattern(WHITE, BLACK)
    assert pattern.pattern_at(point(0, 0, 0)) == WHITE
    assert pattern.pattern_at(point(0, 0, 1)) == WHITE
    assert pattern.pattern_at(point(0, 0, 2)) == WHITE


def test_stripe_pattern_alternate_x():
    '''  Scenario: A stripe pattern alternates in x  '''
    pattern = StripePattern(WHITE, BLACK)
    assert pattern.pattern_at(point(0, 0, 0)) == WHITE
    assert pattern.pattern_at(point(0.9, 0, 0)) == WHITE
    assert pattern.pattern_at(point(1, 0, 0)) == BLACK
    assert pattern.pattern_at(point(-0.1, 0, 0)) == BLACK
    assert pattern.pattern_at(point(-1, 0, 0)) == BLACK
    assert pattern.pattern_at(point(-1.1, 0, 0)) == WHITE


def test_stripes_with_object_transformation():
    '''  Scenario: Stripes with an object transformation  '''
    obj = Sphere()
    obj.transform = Matrix.scaling(2, 2, 2)
    pattern = StripePattern(WHITE, BLACK)
    c = pattern.pattern_at_shape(obj, point(1.5, 0, 0))
    assert c == WHITE


def test_stripes_with_pattern_transformation():
    '''  Scenario: Stripes with a pattern transformation  '''
    obj = Sphere()
    pattern = StripePattern(WHITE, BLACK)
    pattern.transform = Matrix.scaling(2, 2, 2)
    # c = pattern.stripe_at_object(obj, point(1.5, 0, 0))
    c = pattern.pattern_at_shape(obj, point(1.5, 0, 0))
    assert c == WHITE


def test_stripes_with_object_and_pattern_transformation():
    '''  Scenario: Stripes with both an object and a a pattern transformation  '''
    obj = Sphere()
    obj.transform = Matrix.scaling(2, 2, 2)
    pattern = StripePattern(WHITE, BLACK)
    pattern.transform = Matrix.translation(0.5, 0, 0)
    c = pattern.pattern_at_shape(obj, point(2.5, 0, 0))
    assert c == WHITE


def test_default_pattern_transformation():
    '''  Scenario: The default pattern transformation  '''
    pattern = TestPattern()
    assert pattern.transform == Matrix.identity_matrix()


def test_assign_transform():
    ''' Scenario: Assigning a transformation  '''
    pattern = TestPattern()
    pattern.transform = Matrix.translation(1, 2, 3)
    assert pattern.transform == Matrix.translation(1, 2, 3)


def test_pattern_with_object_transformation():
    ''' Scenario: A pattern with an object transformation  '''
    shape = Sphere()
    shape.transform = Matrix.scaling(2, 2, 2)
    pattern = TestPattern()
    c = pattern.pattern_at_shape(shape, point(2, 3, 4))
    assert c == color(1, 1.5, 2)


def test_pattern_with_pattern_transformatio():
    '''  Scenario: A pattern with a pattern transformation  '''
    shape = Sphere()
    pattern = TestPattern()
    pattern.transform = Matrix.scaling(2, 2, 2)
    c = pattern.pattern_at_shape(shape, point(2, 3, 4))
    assert c == color(1, 1.5, 2)


def test_pattern_with_object_and_pattern_transformation():
    '''  Scenario: A pattern with both an object and a pattern transformation  '''
    shape = Sphere()
    shape.transform = Matrix.scaling(2, 2, 2)
    pattern = TestPattern()
    pattern.transform = Matrix.translation(0.5, 1, 1.5)
    c = pattern.pattern_at_shape(shape, point(2.5, 3, 3.5))
    assert c == color(0.75, 0.5, 0.25)


def test_gradient_between_colors():
    '''  Scenario: A gradient linearly interpolates between colors  '''
    pattern = GradientPattern(WHITE, BLACK)
    assert pattern.pattern_at(point(0, 0, 0)) == WHITE
    assert pattern.pattern_at(point(0.25, 0, 0)) == color(0.75, 0.75, 0.75)
    assert pattern.pattern_at(point(0.5, 0, 0)) == color(0.5, 0.5, 0.5)
    assert pattern.pattern_at(point(0.75, 0, 0)) == color(0.25, 0.25, 0.25)


def test_ring_extends_in_x_and_z():
    '''  Scenario: A ring should extend in both x and z  '''
    pattern = RingPattern(WHITE, BLACK)
    pattern.pattern_at(point(0, 0, 0)) == WHITE
    pattern.pattern_at(point(1, 0, 0)) == BLACK
    pattern.pattern_at(point(0, 0, 1)) == BLACK
    # 0.708 = just lightly more than sqrt(2)/2
    pattern.pattern_at(point(0.708, 0, 0.708)) == BLACK
