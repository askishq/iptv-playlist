logo = "https://i.postimg.cc/WzMrTGFJ/20260624-154406.jpg"

channels = [
    ("FIFA 2026 1", "https://prod-cdn01-live.toffeelive.com/live/FIFA-2026/index.m3u8?edge-cache-token=Expires=1782373269URLPrefix=aHR0cHM6Ly9wcm9kLWNkbjAxLWxpdmUudG9mZmVlbGl2ZS5jb20~Signature=ETR9gt1r4keKvdtFS38PYlOqYSMV1JtcKkctph4wDsnXHvLWV8LlbKqq9hv2BcEJeu2rOjWDxno-CSkTysOxAw"),

    ("FIFA 2026 2", "https://prod-cdn01-live.toffeelive.com/live/FIFA-2026-2/index.m3u8?edge-cache-token=Expires=1782373269URLPrefix=aHR0cHM6Ly9wcm9kLWNkbjAxLWxpdmUudG9mZmVlbGl2ZS5jb20Starts=1782286869Signature=ETR9gt1r4keKvdtFS38PYlOqYSMV1JtcKkctph4wDsnXHvLWV8LlbKqq9hv2BcEJeu2rOjWDxno-CSkTysOxAw"),

    ("FIFA 2026 4", "https://prod-cdn01-live.toffeelive.com/live/FIFA-2026-4/index.m3u8?edge-cache-token=Expires=1782373269URLPrefix=aHR0cHM6Ly9wcm9kLWNkbjAxLWxpdmUudG9mZmVlbGl2ZS5jb20~Signature=ETR9gt1r4keKvdtFS38PYlOqYSMV1JtcKkctph4wDsnXHvLWV8LlbKqq9hv2BcEJeu2rOjWDxno-CSkTysOxAw"),

    ("FIFA 2026 5", "https://prod-cdn01-live.toffeelive.com/live/FIFA-2026-5/index.m3u8?edge-cache-token=Expires=1782373269URLPrefix=aHR0cHM6Ly9wcm9kLWNkbjAxLWxpdmUudG9mZmVlbGl2ZS5jb20~Signature=ETR9gt1r4keKvdtFS38PYlOqYSMV1JtcKkctph4wDsnXHvLWV8LlbKqq9hv2BcEJeu2rOjWDxno-CSkTysOxAw"),

    ("FIFA 2026 6", "https://prod-cdn01-live.toffeelive.com/live/FIFA-2026-6/index.m3u8?edge-cache-token=Expires=1782373269URLPrefix=aHR0cHM6Ly9wcm9kLWNkbjAxLWxpdmUudG9mZmVlbGl2ZS5jb20~Signature=ETR9gt1r4keKvdtFS38PYlOqYSMV1JtcKkctph4wDsnXHvLWV8LlbKqq9hv2BcEJeu2rOjWDxno-CSkTysOxAw"),
]

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n\n")

    for name, url in channels:
        f.write(f'#EXTINF:-1 tvg-logo="{logo}",{name}\n')
        f.write(url + "\n\n")
