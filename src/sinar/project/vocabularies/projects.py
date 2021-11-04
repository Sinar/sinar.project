# -*- coding: utf-8 -*-

from plone import api
from plone.dexterity.interfaces import IDexterityContent
from sinar.project import _
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


def make_terms(items):
    """ Create zope.schema terms for vocab from tuples """
    terms = [ SimpleTerm(value=pair[0], token=pair[0], title=pair[1]) for pair in items ]
    return terms

@implementer(IVocabularyFactory)
class Projects(object):
    """
    """

    def __call__(self, context):
        brains = api.content.find(portal_type='Project')

        # Create a list of tuples (UID, Title) of results
        result = [ (brain["UID"], brain["Title"]) for brain in brains ]

        terms = make_terms(result)
        return SimpleVocabulary(terms)

ProjectsFactory = Projects()
