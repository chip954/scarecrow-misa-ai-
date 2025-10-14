from scarecrow_misa import metrics as m

def test_continuity_bounds():
    v1, v2 = [1.0, 0.0], [0.0, 1.0]
    c = m.continuity(v1, v2)
    assert 0.0 <= c <= 1.0

def test_corrigibility_monotone():
    assert m.corrigibility([1.0, 0.8, 0.7, 0.7, 0.5]) >= 0.75