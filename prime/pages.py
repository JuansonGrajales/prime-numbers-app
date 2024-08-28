from flask import Blueprint, jsonify

bp = Blueprint('pages', __name__)

@bp.route('/')
def home():
    return 'Hello, World!'

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

@bp.route('/primes/<int:limit>', methods=['GET'])
def get_primes(limit: int) -> dict:
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return jsonify(primes)