import os
from typing import List, Dict

import hydra_agent.utils.system
from hydra_agent.ring import Ring
from hydra_agent.utils.system import run_command


class LicenseManager(Ring):
    def __init__(self, config: Dict):
        super().__init__(config)

    """Получение лицензии из Центра лицензирования
  
        --company <значение>
            Наименование огранизации.
        --last-name <значение>
            Фамилия пользователя.
        --first-name <значение>
            Имя пользователя.
        --middle-name <значение>
            Отчество пользователя.
        --email <значение>
            Адрес электронной почты пользователя.
        --country <значение>
            Обязательный параметр Наименование страны.
        --zip-code <значение>
            Обязательный параметр Почтовый индекс.
        --region <значение>
            Наименование области/республики/края/штата.
        --district <значение>
            Наименование района.
        --town <значение>
            Обязательный параметр Наименование города.
        --street <значение>
            Обязательный параметр Наименование улицы.
        --house <значение>
            Номер дома/квартала/владения.
        --building <значение>
            Корпус/строение/секция.
        --apartment <значение>
            Квартира/офис.

        --serial <значение>
            Обязательный параметр Регистрационный номер.

        --pin <значение>
            Пин-код. Если не указано, будет ожидаться ввод пин-кода.
        --previous-pin <значение>
            Старый пин-код. Требуется для повторной регистрации лицензии.
            
        --path <значение>
            Путь к файлам лицензий.
        --validate <значение>
            Задает необходимо ли проверять корректность данных об устройствах, получаемых от системы. По умолчанию данные не проверяются.
    """

    def activate(self, license_info: dict, serial: str, pin: str, previous_pin: str = '', path: str = '',
                 validate: bool = False) -> bool:
        """Activates license"""

        pass

    def get(self, name: str, path: str = '') -> bytes:
        """Returns license file"""

        temp_file = hydra_agent.utils.system.temp_file_name()
        args = [self.path, 'license', 'get', '--name', name.strip(), '--license', temp_file]
        if path:
            args.extend(['--path', path.strip()])
        try:
            run_command(args)
            with open(temp_file, 'rb') as f:
                lic = f.read()
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        return lic

    def info(self, name: str, path: str = '') -> str:
        """Returns license info"""

        args = [self.path, 'license', 'info', '--name', name.strip()]
        if path:
            args.extend(['--path', path.strip()])
        return run_command(args)

    def list(self, path: str = '') -> List[str]:
        """Returns list of licenses"""

        args = [self.path, 'license', 'list']
        if path:
            args.extend(['--path', path.strip()])
        r = run_command(args)
        return r.split()

    def put(self, license: bytes, path: str = '') -> bool:
        """Adds license file to storage"""

        license_file = hydra_agent.utils.system.temp_file_name()
        with open(license_file, 'wb') as f:
            f.write(license)
        args = [self.path, 'license', 'put', '--license', license_file]
        if path:
            args.extend(['--path', path.strip()])
        try:
            run_command(args)
        finally:
            if os.path.exists(license_file):
                os.remove(license_file)
        return True

    def remove(self, name: str, path: str = '') -> bool:
        """Removes license file from storage"""

        args = [self.path, 'license', 'remove', '--name', name.strip(), '--all']
        if path:
            args.extend(['--path', path.strip()])
        run_command(args)
        return True

    def validate(self, name: str, path: str = '') -> bool:
        """Validates license"""

        args = [self.path, 'license', 'validate', '--name', name.strip()]
        if path:
            args.extend(['--path', path.strip()])
        run_command(args)
        return True
