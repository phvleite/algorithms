import pytest
from challenges.challenge_encrypt_message import encrypt_message

MOCK_MESSAGES_KEYS = [
    ("ABCDEF", "B"),
    (123456, 3),
    ("ABCDEF", -1, "FEDCBA"),
    ("ABCDEF", 3, "CBA_FED"),
    ("ABCDEF", 4, "FE_DCBA"),
]


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(MOCK_MESSAGES_KEYS[0][0], MOCK_MESSAGES_KEYS[0][1])

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(MOCK_MESSAGES_KEYS[1][0], MOCK_MESSAGES_KEYS[1][1])

    assert (
        encrypt_message(MOCK_MESSAGES_KEYS[2][0], MOCK_MESSAGES_KEYS[2][1])
        == MOCK_MESSAGES_KEYS[2][2]
    )

    assert (
        encrypt_message(MOCK_MESSAGES_KEYS[3][0], MOCK_MESSAGES_KEYS[3][1])
        == MOCK_MESSAGES_KEYS[3][2]
    )

    assert (
        encrypt_message(MOCK_MESSAGES_KEYS[4][0], MOCK_MESSAGES_KEYS[4][1])
        == MOCK_MESSAGES_KEYS[4][2]
    )
