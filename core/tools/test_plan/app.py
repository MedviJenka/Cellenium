import pyChatGPT


TOKEN = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..WFeDwCDx-9WU6Fvf.nxTnllgSbyXngaR3wWZWS43xtvo8GlNegteHBYeUzCwr8gvdNfjYgyNLdFt9A8E7Gk2uir6aj1DoGbdAeudFuwXrFXnNonrYAqQtslkwuI3zZjb4TTazaU6mQxcOV6ZE1oD24yCLyxCEkrTF2zZE2egTZHEc0t8KLfOLRM3sHRGdwc-9NCSEAe9ZpHNY8XQe-h63cGahJf-_uEoOZIpUkvo8x2Tr4tokNx90JEgD0T7SQkmqSt4_b1dfma5Tew6BRgSaVlW-DbuxMyw3hLO2aSfXPGFOA_hLEmBBdsK7r2ZqmDBOPW88tgA5Vybt2YoQyU4UPcfivdxIsItVyVvA_wgMeVPADjUporyBOJDZjSaogfUo4CUa3cB58MutlOLoqw3xC529bW69zxyzoycHo7mVVlIaH9q2waVp7Po6OZCgCUqhmuvKMKXqNYHeCHzb75r8AGVo9XMQJICuRkGD0yymxnhZdh8rfRKrKjv6xn21ecFSVikAPB3qgnLIz9Q1Ezj--zsvsGLsgwlFHIN21zHzym8BzX3jdnOEp9MCecrPsLmYrSMgObPx_ZLaSoEu7a_ELh-VTTS_r5UHWnGuoEWmetEcxVlr-YMsnI6CXbpyt2tTt8od-gRhJaz1p94MR9kGisq2Ah9-5Ma2-vr1Pp4g_6qxbLVa4lVcI2rVDVRDU4-WMfKWRwJQgNOy6LgXLxkRfyNQH9lPWIpeTYEQgLqo80gJONoIAHwjScqIODhKB7MOBKtPqWX4OjPHDr_oJt2eGKYoGWFyAvGEdDaw6DKqLjAAr8tnxDDMbe7z9zOGLETbyUK2YGpzAEHwrEJ43wE9IvxDVFoU8-ednLcKZgcJovGn171WD-llnatm-Hmk48YX2Yi_Ak6iz2_jlSArDb3mU56hZRV8Gf5lrTTXv1eEiysxTS0qQdBMaOhl_TCSQgXYibbkk99FzECyxHJKvHnwB2wPS3OMpLZ1i9KagcGMaleYkgPpcunDMEbO5k7xo8ImeoVPMHRgIR7qAtJmwLIPx5xlX643pemUtvIIH--MsSvfLwhHMr_kvI5LSy0d5OJ2vHNi2_Mm2xX9yZKGdvBP-82Ycfda3bmq7l3T6hiS5h2dUKXnqj3XopRHbMrAn9SuGDHy0jQh727K3CZ5m_b4h9OT1doy4cyuMjA07YonFORcczO-4NKdndoF4R0RrxdDanJNXR3G--WyQMCMc-RQy8U7egfbS7zVORiyXndAH27AWGXSq8dVALFLGD-db29xAUHC2NvfzR0F78x-bBk0xvi35BRIf-MhQYr7UIjG0jrZjZ_PRNiH7seKOHFT2HsitX1ZnFpNaTulX80w1Do4qK8fKdg0PC65Bszp3LpBygsBYxOSONzyefzw7Fr3qP_2sA-OqBXpdvgKim-C8k-IbeN9yUyFHz761iptyB2eUE2YV0Rf5vOILGfJ1BbxQDmNJBh-OroWSQz_ZQDQN88ruJkf0m3RwM7txURCmV958MjvYkKmRqbu5Qcdh6DUQtR1fXlj5Px4az0T5PT46qiKZF3nqPo9jix88Ym3kTX94QYrPVOSfx798yZObMTJRohpbW_tO8IaJizihrNeRFf8tlzn0a09LB8IoBIben3_bB7na_fW8iQK3uXafcOmSo-TmFERab9QF-W9FZ33KR4cAiTv_p-Kn8BRVke51Zb1Jvq73WtpJ9cAYJX4KEjo1rz1BFGZnFmJuezLSuH3-4Os_u1eJ9bI-0O7uNtr1LAxWNTsTjjlUfXM-53tfh_z3EZz6GnzyuXOev1DJSyGGrhBnP6uy91dukYWCwOeJngyPgjPlp4mz0DWj8UongU0iCVftYxsytTpEJY_hTpawS3HfErpCZ0X3InLclplVDQDSo8HY2UYJnUJYi4NWcdzGdw1BrhySYmE8zqQsYEvnT9-yMCZcDq0ioDquWR0X-Zvdufs5KA2vnT8lFq-MK22VXcKahMghr7WVZ_60Aeus3AfxH7Ad9mNJSB38xhxq1l_PTVxpO8Wo7E3jN-LiyGv4v0MxPp4CXWsLosH0D3Ri1b-i94izaxFCOBOqSsYBi0Db1yM0QImAckqZTqL2FDzTJnjLcMgHSGvpVttIxGyKeu6oo8kMAJSmdKGDX0xJxb9ZX5Rhe-Efldk-OWVLV_YpZCVWUKCtvxLdRNass0TQ5pNXI-muduzKP0kIYO0aU5RgSKsYIJ-3H8EK3q0dNJuudAUp7wJACAWPW668TUeIc3lkWLcdKOTixiMrymZ5klOs9p3Mqf94q2PtAo9j9g5sDQIme40y44EEIu_mPKnrdO4-Gu1fnV6RSnqXNxO8kHWC9WaPJpNptern3n0qUtgky62dQd3riYlQ94rV7V5hFfYuysrON0k7lAfQPnIpqaiwBMmR1XedHCMGcyYMNeirXWmSMIhgcN9w7sksDsZYUYSmuRV77MQ_qHLVXJmCMPbJy8b0I4ZS70yt8IeXsZGLH_Znv4YrZ6Yo_wAR5a_6Tw4tdzRTXfQX8YuGBa6k7nadFag8mMgao8_6iKQrWuGmJmthx2L-OOzEMylp6xTVPH2kyE5kfYIJ0BS3zjxgSGBA_qekE96vNbPgzXVvS8x56YKLaNKIYPaW-FaVN2tSUAV-oJICo3Elbd0ELim62IGiNWv5CEsBGPq6qjKhYgpmw.E6AupsypDleD02H_1YN7ng"


def ai_test_plan(text: str) -> None:
    session_api = pyChatGPT.ChatGPT(session_token=TOKEN)
    response = session_api.send_message(text)
    result = "".join(response.get(f'write a test plan for {text}'))
    print(result)