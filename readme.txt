api truy cập qua 2 url tương ứng với 2 loại: cử chỉ và hành động. giao tiếp qua http post.
	- lấy cử chỉ tay: localhost:5000/predict_gesture 
	- lấy hành động: localhost:5000/predict_activity
	- dữ liệu cần gửi sang có dạng 1 danh sách các bản ghi mỗi bản ghi tương ứng với 1 dòng dưới đây. Về trường timestamps cần bổ sung thêm vào json của mỗi bản ghi ngay khi anh nhận được bản ghi đó từ đồng hồ.
{'yaw': -157.6705, 'pitch': -4.33582, 'roll': -2.451883, 'Ax': 0, 'Ay': 485, 'Az': 7381, 'timestamps': 1542884104.3810017}
{'yaw': -157.7411, 'pitch': -4.701654, 'roll': -1.870299, 'Ax': -53, 'Ay': 630, 'Az': 7189, 'timestamps': 1542884104.3893933}
{'yaw': -157.8128, 'pitch': -5.099143, 'roll': -1.229501, 'Ax': -92, 'Ay': 793, 'Az': 6948, 'timestamps': 1542884104.3895116}
{'yaw': -157.888, 'pitch': -5.491229, 'roll': -0.536322, 'Ax': -101, 'Ay': 972, 'Az': 6662, 'timestamps': 1542884104.3895922}
{'yaw': -157.9806, 'pitch': -5.876004, 'roll': 0.203376, 'Ax': -78, 'Ay': 1154, 'Az': 6383, 'timestamps': 1542884104.3896697}
{'yaw': -158.0988, 'pitch': -6.23351, 'roll': 1.001146, 'Ax': -47, 'Ay': 1327, 'Az': 6080, 'timestamps': 1542884104.3897498}
{'yaw': -158.2434, 'pitch': -6.561466, 'roll': 1.850324, 'Ax': -25, 'Ay': 1495, 'Az': 5765, 'timestamps': 1542884104.3957014}
{'yaw': -158.4008, 'pitch': -6.87749, 'roll': 2.732575, 'Ax': -26, 'Ay': 1640, 'Az': 5467, 'timestamps': 1542884104.402717}
{'yaw': -158.5817, 'pitch': -7.214567, 'roll': 3.642598, 'Ax': -64, 'Ay': 1763, 'Az': 5226, 'timestamps': 1542884104.4223776}
{'yaw': -158.7815, 'pitch': -7.569189, 'roll': 4.560029, 'Ax': -128, 'Ay': 1881, 'Az': 5010, 'timestamps': 1542884104.4298563}
{'yaw': -158.9735, 'pitch': -7.964042, 'roll': 5.493948, 'Ax': -213, 'Ay': 2002, 'Az': 4802, 'timestamps': 1542884104.4378462}
{'yaw': -159.1587, 'pitch': -8.391348, 'roll': 6.43947, 'Ax': -298, 'Ay': 2115, 'Az': 4570, 'timestamps': 1542884104.445374}
{'yaw': -159.3449, 'pitch': -8.828246, 'roll': 7.394055, 'Ax': -359, 'Ay': 2192, 'Az': 4306, 'timestamps': 1542884104.4516056}
{'yaw': -159.5355, 'pitch': -9.249805, 'roll': 8.376926, 'Ax': -367, 'Ay': 2264, 'Az': 3959, 'timestamps': 1542884104.4568706}
{'yaw': -159.7241, 'pitch': -9.641657, 'roll': 9.389371, 'Ax': -360, 'Ay': 2295, 'Az': 3639, 'timestamps': 1542884104.4693735}
{'yaw': -159.9208, 'pitch': -9.992014, 'roll': 10.44846, 'Ax': -342, 'Ay': 2333, 'Az': 3268, 'timestamps': 1542884104.4786673}

	- dữ liệu api trả về:
		+ cử chỉ: 1 trong 4 giá trị [ 'up', 'down', 'left', 'right']
		+ hành động: 1 trong các hàng động: ['walking', 'running', 'standing', 'sitting']

	- Mapping hành động và mã HEX:
		- up: 0xa10
		- down: 0xa20
		- left: 0xa30
		- right: 0xa40
		- walking: 0xa50
		- running: 0xa60
		- standing: 0xa70
		- sitting: 0xa80

