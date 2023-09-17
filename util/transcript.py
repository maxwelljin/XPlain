# Author: ray
# Date: 9/16/23
# Description:

from youtube_transcript_api import YouTubeTranscriptApi

from llm.gpt import call_gpt


def get_transcript_detail(video_id: str) -> list:
    return YouTubeTranscriptApi.get_transcript(video_id)


def get_transcript_str(video_id: str) -> str:
    trans_list = get_transcript_detail(video_id=video_id)
    trans_str = transcript_to_str(transcript=trans_list)
    return trans_str


def transcript_to_str(transcript: list) -> str:
    str_trans = ""
    for i in transcript:
        str_trans += i["text"].replace("\n", " ") + " "
    return str_trans


def get_summarized_transcript(video_id: str) -> str:
    trans_str = get_transcript_str(video_id=video_id)

    appro_l = len(trans_str.split())

    answer_dict = call_gpt(role_description="you are a good assistant",
                           prompt=f"Summarize the following passage: \n{trans_str}")
    answer = answer_dict["content"]
    return answer
