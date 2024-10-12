from flask import Blueprint, jsonify, request
from ..repositories.swatch_repository import SwatchRepository
from ..strategies.rgb_strategy import RGBStrategy
from ..strategies.hsl_strategy import HSLStrategy
from ..strategies.brgb_strategy import BRGBStrategy
from ..strategies.hex_strategy import HexStrategy

# @see https://flask.palletsprojects.com/en/2.4.x/blueprints/
swatches_blueprint = Blueprint('swatches', __name__)
 
# Initialize the swatch repository
swatches = SwatchRepository()
# Add RGB and HSL swatches for demo
swatches.add_swatch(RGBStrategy("Red", red=255, green=0, blue=0))
swatches.add_swatch(HSLStrategy("Green", hue=120, saturation=100, lightness=50))
 
@swatches_blueprint.route('/', methods=['GET'])
def index(): 
    return jsonify(swatches.get_swatches()), 200
 
@swatches_blueprint.route('/regenerate', methods=['PUT'])
def regenerate_swatches():
    # get request data
    body = request.get_json()
    type = body['type']

    try:
        # validate request data
        if not body or 'type' not in body:
            return jsonify({"error": "Invalid request data"}), 400
         
        # validate attributes
        if type == 'rgb' and ('red' not in body or 'green' not in body or 'blue' not in body):
            return jsonify({"error": "Invalid attributes"}), 400

        if type == 'hsl' and ('hue' not in body or 'saturation' not in body or 'lightness' not in body):
            return jsonify({"error": "Invalid attributes"}), 400
        
        if type == 'brgb' and ('blue' not in body or 'green' not in body or 'red' not in body):
            return jsonify({"error": "Invalid attributes"}), 400
        
        if type == 'hex' and ('hex' not in body):
            return jsonify({"error": "Invalid attributes"}), 400

        if type == 'rgb':
            swatches.add_swatch(RGBStrategy(body['name'], red=body['red'], green=body['green'], blue=body['blue']))
        elif type == 'hsl':
            swatches.add_swatch(HSLStrategy(body['name'], hue=body['hue'], saturation=body['saturation'], lightness=body['lightness']))
        elif type == 'brgb':
            swatches.add_swatch(BRGBStrategy(body['name'], blue=body['blue'], green=body['green'], red=body['red']))
        elif type == 'hex':
            swatches.add_swatch(HexStrategy(body['name'], hex_value=body['hex']))
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    return jsonify(swatches.get_swatches()), 200