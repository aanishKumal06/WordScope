from django.views.generic import View
from django.shortcuts import render
import re


class TextProcessing:
    def clean_paragraph(self, paragraph):
        cleaned = re.sub(r"[^A-Za-z0-9\s]", "", paragraph)
        cleaned = re.sub(r"\s+", " ", cleaned)
        return cleaned

    def count_sentences(self, paragraph):
        sentences = paragraph.split(".")
        return len(sentences) - 1

    def count_words(self, words):
        counter_dict = {}
        for word in words:
            word = word.lower().strip()
            if word:
                counter_dict[word] = counter_dict.get(word, 0) + 1
        return counter_dict

    def sort_dict(self, counter_dict):
        return dict(
            sorted(counter_dict.items(), key=lambda item: item[1], reverse=True)
        )


class HomePage(View):
    def get(self, request):
        return render(request, "index.html")


class TextAnalysisView(TextProcessing, View):
    def get(self, request):
        return render(request, "text_analysis.html")

    def post(self, request):
        paragraph = request.POST.get("paragraph")
        if not paragraph:
            context = {
                "word_count": 0,
                "character_count": 0,
                "sentence_count": 0,
                "sorted_dict": {},
                "input_text": "",
            }
        else:
            paragraph_cleaned = self.clean_paragraph(paragraph)
            words = paragraph_cleaned.split(" ")
            sentence_count = self.count_sentences(paragraph)
            word_count = len(words) - 1
            character_count = len(paragraph)
            counter_dict = self.count_words(words)
            sorted_dict = self.sort_dict(counter_dict)

            context = {
                "word_count": word_count,
                "character_count": character_count,
                "sentence_count": sentence_count,
                "sorted_dict": sorted_dict,
                "input_text": paragraph,
            }

        return render(request, "text_analysis.html", context)


class TextStatsView(TextProcessing, View):
    def get(self, request):
        return render(request, "text_stats.html")

    def post(self, request):
        paragraph = request.POST.get("paragraph")
        if not paragraph:
            context = {
                "word_count": 0,
                "character_count": 0,
                "sentence_count": 0,
                "input_text": "",
            }
        else:
            paragraph_cleaned = self.clean_paragraph(paragraph)
            words = paragraph_cleaned.split(" ")
            sentence_count = self.count_sentences(paragraph)
            word_count = len(words) - 1
            character_count = len(paragraph)

            context = {
                "word_count": word_count,
                "character_count": character_count,
                "sentence_count": sentence_count,
                "input_text": paragraph,
            }

        return render(request, "text_stats.html", context)


class WordFrequencyView(TextProcessing, View):
    def get(self, request):
        return render(request, "word_frequency.html")

    def post(self, request):
        paragraph = request.POST.get("paragraph")
        if not paragraph:
            context = {
                "sorted_dict": {},
                "input_text": "",
            }
        else:
            paragraph_cleaned = self.clean_paragraph(paragraph)
            words = paragraph_cleaned.split(" ")
            counter_dict = self.count_words(words)
            sorted_dict = self.sort_dict(counter_dict)

            context = {"sorted_dict": sorted_dict, "input_text": paragraph}

        return render(request, "word_frequency.html", context)