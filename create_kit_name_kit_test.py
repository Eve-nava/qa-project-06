import sender_stand_request
import data

# Crea el cuerpo del kit con el nombre especificado
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

# Prueba positiva (espera código 201)
def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    response_data = response.json()
    assert response.status_code == 201
    assert response_data["name"] == name

# Prueba negativa (espera código 400)
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400

# Prueba negativa sin campo "name"
def negative_assert_no_name():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400

# --- Casos de prueba ---

def test_create_kit_1_letter_name_get_success_response():
    positive_assert("a")

def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("a" * 511)

def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400("")

def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert_code_400("a" * 512)

def test_create_kit_with_special_symbols_get_success_response():
    positive_assert("\"№%@\",")

def test_create_kit_with_spaces_in_name_get_success_response():
    positive_assert(" A Aaa ")

def test_create_kit_with_numbers_in_name_get_success_response():
    positive_assert("123")

def test_create_kit_without_name_field_get_error_response():
    negative_assert_no_name()

def test_create_kit_with_number_type_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
