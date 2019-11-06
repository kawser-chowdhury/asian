"""Flexible page."""
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core import blocks as streamfield_blocks

from streams import blocks
from streams.blocks import TwoColumnBlock, ColumnBlock

class FlexPage(Page):
    """Flexibile page class."""

    template = "flex/flex_page.html"
    subpage_types = ['flex.FlexPage', 'contact.ContactPage']
    parent_page_types = [
        'flex.FlexPage',
        'home.HomePage',
    ]
    content = StreamField(
        [
            ("title", blocks.HeaderTitleBlock()),
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("image", blocks.ImageBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
            ("button", blocks.ButtonBlock()),
            ("simple_card", blocks.SimpleCardBlock()),
            ("carousel", blocks.CarouselBlock()),
            ("char_block", streamfield_blocks.CharBlock(
                required=True,
                help_text='Oh wow this is help text!!',
                min_length=10,
                max_length=50,
                template="streams/char_block.html",
            )),
            ("simple_column", ColumnBlock()),
            ('two_columns', TwoColumnBlock()),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta:  # noqa 
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"