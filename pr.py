import segno

qrcode = segno.make_qr(
    """
        • I tried to do the same, but my eyes wanted to
        stare at her more and refused to turn away. Look elsewhere, you stupid
        idiot, or she will think that you have some problem with your eyes or
        worse, with your brains! I told myself, but my eyes just did not cooperate.
    """

)
print(qrcode)

qrcode.save(
    "borderless_qrcode.svg",
    scale=2,
    border=2,
)