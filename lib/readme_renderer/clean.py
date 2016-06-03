# Copyright 2014 Donald Stufft
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, division, print_function

import bleach


ALLOWED_TAGS = [
    # Bleach Defaults
    "a", "abbr", "acronym", "b", "blockquote", "code", "em", "i", "li", "ol",
    "strong", "ul",

    # Custom Additions
    "br", "cite", "col", "colgroup", "dd", "div", "dl", "dt", "h1", "h2", "h3",
    "h4", "h5", "h6", "hr", "img", "p", "pre", "span", "sub", "sup", "table",
    "tbody", "td", "th", "thead", "tr", "tt", "kbd", "var",
]

ALLOWED_ATTRIBUTES = {
    # Bleach Defaults
    "a": ["href", "title"],
    "abbr": ["title"],
    "acronym": ["title"],

    # Custom Additions
    "*": ["id"],
    "hr": ["class"],
    "img": ["src"],
    "span": ["class"],
}

ALLOWED_STYLES = []


def clean(html, tags=None, attributes=None, styles=None):
    if tags is None:
        tags = ALLOWED_TAGS
    if attributes is None:
        attributes = ALLOWED_ATTRIBUTES
    if styles is None:
        styles = ALLOWED_STYLES

    def nofollow(attrs, new=False):
        if attrs["href"].startswith("mailto:"):
            return attrs
        attrs["rel"] = "nofollow"
        return attrs

    # Clean the output using Bleach
    cleaned = bleach.clean(
        html,
        tags=tags,
        attributes=attributes,
        styles=styles,
    )

    # Bleach Linkify makes it easy to modify links, however, we will not be
    # using it to create additional links.
    cleaned = bleach.linkify(
        cleaned,
        callbacks=[
            lambda attrs, new: attrs if not new else None,
            nofollow,
        ],
        skip_pre=True,
        parse_email=False,
    )

    return cleaned
