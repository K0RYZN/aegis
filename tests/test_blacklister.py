from Blacklister import host_matches


def test_exact_domain_match():
    assert host_matches("doubleclick.net", "doubleclick.net")


def test_subdomain_match():
    assert host_matches("ad.doubleclick.net", "doubleclick.net")


def test_deep_subdomain_match():
    assert host_matches("stats.g.doubleclick.net", "doubleclick.net")


def test_does_not_match_similar_fake_domain():
    assert not host_matches("notdoubleclick.net", "doubleclick.net")


def test_does_not_match_domain_hidden_inside_other_domain():
    assert not host_matches("doubleclick.net.evil.com", "doubleclick.net")


def test_case_insensitive_match():
    assert host_matches("AD.DOUBLECLICK.NET", "doubleclick.net")


def test_trailing_dot_match():
    assert host_matches("ad.doubleclick.net.", "doubleclick.net")
