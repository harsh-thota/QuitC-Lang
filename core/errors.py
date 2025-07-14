from runtime.sarcastic_messages import get_sarcastic_message

class SarcasticError(Exception):

    def __init__(self, error_type: str, context: str = None, line: int = None):
        self.error_type = error_type
        self.context = context
        self.line = line
        self.message = self._format_message()
        super().__init__(self.message)

    def _format_message(self):
        msg = get_sarcastic_message(self.error_type)
        if self.context:
            msg += f" [Context: {self.context}]"
        if self.line is not None:
            msg = f"[LINE {self.line}] " + msg

        return msg