from flask import make_response, jsonify, current_app
from flask_login import login_required
from flask_restful import Resource

from utils import ApiRequestError


class YoutubePopularResource(Resource):
    @login_required
    def get(self):
        try:
            service = current_app.config['YOUTUBE_SERVICE']
            result = service.get_popular_channels()
        except ApiRequestError as er:
            return make_response(jsonify({'message': str(er.message)}), er.status_code)

        return make_response(jsonify(result), 200)
