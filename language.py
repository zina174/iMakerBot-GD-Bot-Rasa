import typing
from typing import Any, Optional, Text, Dict, List, Type

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.training_data.message import Message
from translation import TranslationServiceClient


#import six
#from google.cloud import translate

if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata


class LanguageHandler(Component):
    """A new component"""

    # Which components are required by this component.
    # Listed components should appear before the component itself in the pipeline.
    @classmethod
    def required_components(cls) -> List[Type[Component]]:
        """Specify which components need to be present in the pipeline."""

        return []

    # Defines the default configuration parameters of a component
    # these values can be overwritten in the pipeline configuration
    # of the model. The component should choose sensible defaults
    # and should be able to create reasonable results with the defaults.
    defaults = {}

    # Defines what language(s) this component can handle.
    # This attribute is designed for instance method: `can_handle_language`.
    # Default value is None which means it can handle all languages.
    # This is an important feature for backwards compatibility of components.
    supported_language_list = None

    # Defines what language(s) this component can NOT handle.
    # This attribute is designed for instance method: `can_handle_language`.
    # Default value is None which means it can handle all languages.
    # This is an important feature for backwards compatibility of components.
    not_supported_language_list = None


    def __init__(self, component_config: Optional[Dict[Text, Any]] = None) -> None:
        super().__init__(component_config)

        #translation service variables
        self.client = TranslationServiceClient()
        """self.location = "global"
        self.project_id = 'still-resource-318401'
        self.parent = f"projects/{self.project_id}/locations/{self.location}"""

    def train(
        self,
        training_data: TrainingData,
        config: Optional[RasaNLUModelConfig] = None,
        **kwargs: Any,
    ) -> None:
        """Train this component.

        This is the components chance to train itself provided
        with the training data. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.train`
        of components previous to this one."""
        pass


    def process(self, message: Message, **kwargs: Any) -> None:
        """Process an incoming message.

        This is the components chance to process an incoming
        message. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.process`
        of components previous to this one."""

        text = Text(message.get('text')) #handle text as a Text object rather than a simple string for rasa version compatibilty issues else it won't work
        
        #language detection request
        #detected_languages = self.client.pred_langid(text)
        detected_language = self.client.pred_langid(text)
        #detected_language = detected_languages[0]


        # Detail on supported types can be found here:
        # https://cloud.google.com/translate/docs/supported-formats
        
        #translating to french when necessary
        if detected_language == 'fr':
            response = self.client.Translate_input(text)
            #changing the input message's text after translation
            message.set('text', Text(response))
        elif detected_language == 'ar':
            response = self.client.Translate_arabic_input(text)
            #changing the input message's text after translation
            message.set('text', Text(response))
        #setting a language entity so it can be used by custom actions
        entity = {
            'value': detected_language,
            #'confidence': detected_language.confidence,
            'entity': 'language',
            'extractor': 'LanguageHandler'
        }

        message.set("entities", [entity], add_to_output=True)

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this component to disk for future loading."""

        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Text,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any,
    ) -> "Component":
        """Load this component from file."""

        if cached_component:
            return cached_component
        else:
            return cls(meta)
