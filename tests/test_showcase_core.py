from friday_open.capability_router import route
from friday_open.context_manager import compact
from friday_open.web_repair import repair_html


def test_router_keeps_bundle_small():
    result = route("corrija meu html")
    assert result.capabilities == ("capability_control", "web_repair")


def test_context_is_bounded_and_keeps_recent():
    messages = ["x" * 10_000 for _ in range(10)] + ["RECENT-A", "RECENT-B"]
    result = compact(messages, max_chars=40_000, keep_recent_chars=20_000, summary_chars=2_000)
    assert result.compacted is True
    assert result.recent[-2:] == ("RECENT-A", "RECENT-B")
    assert len(result.summary) <= 2_000


def test_html_tail_repair_is_deterministic():
    result = repair_html("<main><section><p>Hello</p>")
    assert result.changed is True
    assert result.confidence >= 0.98
    assert result.output.endswith("</section></main>")


def test_mismatched_html_is_not_guessed():
    result = repair_html("<div><span></div></span>")
    assert result.changed is False
    assert result.ok is False
