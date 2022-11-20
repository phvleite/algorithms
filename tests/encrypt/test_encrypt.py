import pytest
from challenges.challenge_encrypt_message import encrypt_message

MOCK_MESSAGES_KEYS = [
    ("ABCDEF", "B"),
    (123456, 3),
    ("ABCDEF", -1, "FEDCBA"),
    ("ABCDEF", 3, "CBA_FED"),
    ("ABCDEF", 4, "FE_DCBA"),
    ("CHEWBACCA", 20, "CHEWBACCA"),
]


def test_encrypt_message():
    with pytest.raises(TypeError) as err:
        encrypt_message(MOCK_MESSAGES_KEYS[0][0], MOCK_MESSAGES_KEYS[0][1])
        raise TypeError("tipo inválido para key")
    assert err.type is TypeError

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(MOCK_MESSAGES_KEYS[1][0], MOCK_MESSAGES_KEYS[1][1])
        raise TypeError("tipo inválido para message")
    assert err.type is TypeError

    result = encrypt_message(
        MOCK_MESSAGES_KEYS[2][0], MOCK_MESSAGES_KEYS[2][1]
    )
    assert result == MOCK_MESSAGES_KEYS[2][2]

    result = encrypt_message(
        MOCK_MESSAGES_KEYS[3][0], MOCK_MESSAGES_KEYS[3][1]
    )
    assert result == MOCK_MESSAGES_KEYS[3][2]

    result = encrypt_message(
        MOCK_MESSAGES_KEYS[4][0], MOCK_MESSAGES_KEYS[4][1]
    )
    assert result == MOCK_MESSAGES_KEYS[4][2]

    result = encrypt_message(
        MOCK_MESSAGES_KEYS[5][0], MOCK_MESSAGES_KEYS[5][1]
    )
    assert result != MOCK_MESSAGES_KEYS[5][2]
