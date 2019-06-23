import unittest
import os

import youtube_download


class TestYoutubeDownload(unittest.TestCase):
    def setUp(self):
        print("Setting up tests for youtube_download.py...")

    def test_download_mediafile_youtube_working(self):
        # Working and available video.
        result = youtube_download.downloader(
            "https://www.youtube.com/watch?v=ptYBn6Eo_6I"
        )
        print(result)
        self.assertEqual(result, "ptYBn6Eo_6I.mp4")

    def test_download_mediafile_youtube_fail(self):
        # Missing video on YouTube.
        with self.assertRaises(RuntimeError) as cm:
            youtube_download.downloader(
                "https://www.youtube.com/watch?v=2vZgvFIa8y0"
            )  # deleted video
        self.assertTrue(str(cm.exception).__contains__("ERROR"))


if __name__ == '__main__':
    unittest.main()