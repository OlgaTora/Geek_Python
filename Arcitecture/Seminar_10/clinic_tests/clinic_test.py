# import mock
import unittest
from unittest import mock

import pytest
from httpx import AsyncClient
from starlette.testclient import TestClient

from Arcitecture.Seminar_10.clinic.repositories.clients_repository import ClientRepository
from Arcitecture.Seminar_10.clinic.routers import client_router
from Arcitecture.Seminar_10.clinic.schemas.client import Client
from Arcitecture.Seminar_10.clinic.services.app import app


@pytest.fixture
def client():
    client = TestClient(app)
    yield client


def test_get_all_clients(client):
    # [1] Подготовка данных для тестирования
    # Создаем мок-объект для зависимости
    client_repo_mock = mock.AsyncMock(spec=ClientRepository)
    client_repo_mock.get_all.return_value = [
        Client(client_id=1, document="123", surname='test1', firstname='test1', patronymic='test1',
               birthday='2012-01-10'),
        Client(client_id=2, document="131", surname='test2', firstname='test2', patronymic='test2',
               birthday='2012-11-10'),
    ]
    # [2] Исполнение тестируемого метода
    # Создаем объект, который мы будем тестировать

    # _clientController = client_repo_mock.mock_calls
    # app.dependency_overrides[get_db] = override_get_db
    with app.clients_repository.override(client_repo_mock):
        response = client.get('/get-all-clients/')

        assert response.status_code == 200
        data = response.json()
        assert data == [
            {'id': 1, 'document': "123", 'surname': 'test1', 'firstname': 'test1', 'patronymic': 'test1',
             'birthday': '2012-01-10'},
            {'id': 2, 'document': "131", 'surname': 'test2', 'firstname': 'test2', 'patronymic': 'test2',
             'birthday': '2012-11-10'},
        ]


#
# @pytest.fixture
# def clients() -> list[Client]:
#     clients_list = [
#         Client(),
#         Client(),
#         Client()
#     ]
#     return clients_list
#
#
# def test_get_all_clients(clients):
#     # Имитируем поведение зависимости в мок-объекте
#     _mockClientRepository.get_all_clients.return_value = clients
#     operation_result = _clientController.get_all_clients('/get-all-clients/')
# #

#
# class MyObject:
#     def __init__(self, dependency):
#         self.dependency = dependency
#
#     def my_method(self, arg):
#         # какой-то метод, который зависит от зависимости
#         return self.dependency.some_method(arg)

# # Тестируем метод объекта
# result = my_object.my_method("some argument")
# # Проверяем, что метод объекта вызвал метод зависимости с правильным аргументом
# mock_dependency.some_method.assert_called_once_with("some argument")
# # Проверяем, что метод объекта вернул правильный результат
# assert result == 42

#         public void GetAllClientsTest()
#         {
#             // [1] Подготовка данных для тестирования
#
#             List<Client> clientsList = new List<Client>();
#             clientsList.Add(new Client());
#             clientsList.Add(new Client());
#             clientsList.Add(new Client());
#
#             _mockClientRepository.Setup(repository =>
#              repository.GetAll()).Returns(clientsList);
#
#             // [2] Исполнение тестируемого метода
#
#             var operationResult = _clientController.GetAll();
#
#             // [3] Подготовка эталонного результата, проверка результата
#             Assert.IsType<OkObjectResult>(operationResult.Result);
#             var okObjectResult = (OkObjectResult)operationResult.Result;
#             Assert.IsAssignableFrom<List<Client>>(okObjectResult.Value);
#
#             _mockClientRepository.Verify(repository =>
#               repository.GetAll(), Times.AtLeastOnce);
#
#         }


if __name__ == '__main__':
    pytest.main(['-v'])

# ublic class ClientControllerTests
#     {
#
#         private ClientController _clientController;
#         private Mock<IClientRepository> _mockClientRepository;
#
#
#         public ClientControllerTests()
#         {
#             _mockClientRepository = new Mock<IClientRepository>();
#             _clientController = new ClientController(_mockClientRepository.Object);
#         }
#
#
#         [Fact]
#         public void GetAllClientsTest()
#         {
#             // [1] Подготовка данных для тестирования
#
#             List<Client> clientsList = new List<Client>();
#             clientsList.Add(new Client());
#             clientsList.Add(new Client());
#             clientsList.Add(new Client());
#
#             _mockClientRepository.Setup(repository =>
#              repository.GetAll()).Returns(clientsList);
#
#             // [2] Исполнение тестируемого метода
#
#             var operationResult = _clientController.GetAll();
#
#             // [3] Подготовка эталонного результата, проверка результата
#             Assert.IsType<OkObjectResult>(operationResult.Result);
#             var okObjectResult = (OkObjectResult)operationResult.Result;
#             Assert.IsAssignableFrom<List<Client>>(okObjectResult.Value);
#
#             _mockClientRepository.Verify(repository =>
#               repository.GetAll(), Times.AtLeastOnce);
#
#         }
#
#         public static object[][] CorrectCreateClientData =
#         {
#             new object[] { new DateTime(1986, 1, 22), "AA1 B11222", "Иванов1", "Станислав1", "Андреевич1" },
#             new object[] { new DateTime(1986, 1, 22), "AA1 B11222", "Иванов2", "Станислав2", "Андреевич2" },
#             //new object[] { new DateTime(2013, 1, 22), "AA1 B11222", "Иванов3", "Станислав3", "Андреевич3" },
#             new object[] { new DateTime(1986, 1, 22), "AA1 B11222", "Иванов4", "Станислав4", "Андреевич4" },
#             new object[] { new DateTime(1986, 1, 22), "AA1 B11222", "Иванов5", "Станислав5", "Андреевич5" },
#             //new object[] { new DateTime(1986, 1, 22), "AA1 B11222", "Иванов", "", "Андреевич" },
#             new object[] { new DateTime(1986, 1, 22), "AA1 B11222", "Иванов6", "Станислав6", "Андреевич6" },
#             new object[] { new DateTime(1986, 1, 22), "AA1 B11222", "Иванов7", "Станислав7", "Андреевич7" },
#             new object[] { new DateTime(1986, 1, 22), "AA1 B11222", "Иванов8", "Станислав8", "Андреевич8" },
#
#         };
#
#
#         [Theory]
#         [MemberData(nameof(CorrectCreateClientData))]
#         public void CreateClientTest(
#             DateTime birthday, string document, string surName, string firstName, string patronymic)
#         {
#             // [1] Подготовка данных для тестирования
#
#
#             CreateClientRequest createClientRequest = new CreateClientRequest();
#             createClientRequest.Birthday = birthday;
#             createClientRequest.Document = document;
#             createClientRequest.SurName = surName;
#             createClientRequest.FirstName = firstName;
#             createClientRequest.Patronymic = patronymic;
#
#             _mockClientRepository.Setup(repository =>
#             repository.Create(It.IsNotNull<Client>())).Returns(1).Verifiable();
#
#             // [2] Исполнение тестируемого метода
#
#             var operationResult = _clientController.Create(createClientRequest);
#
#             // [3] Подготовка эталонного результата, проверка результата
#             Assert.IsType<OkObjectResult>(operationResult.Result);
#             var okObjectResult = (OkObjectResult)operationResult.Result;
#             Assert.IsAssignableFrom<int>(okObjectResult.Value);
#             _mockClientRepository.Verify(repository =>
#             repository.Create(It.IsNotNull<Client>()), Times.AtLeastOnce());
#         }
#
#         public static object[][] IncorrectCreateClientData =
#         {
#             new object[] { new DateTime(2013, 1, 22), "AA1 B11222", "Иванов3", "Станислав3", "Андреевич3" },
#             new object[] { new DateTime(1986, 1, 22), "AA1 B11222", "Иванов", "", "Андреевич" },
#
#         };
#
#         [Theory]
#         [MemberData(nameof(IncorrectCreateClientData))]
#         public void CreateClientErrorTest(
#             DateTime birthday, string document, string surName, string firstName, string patronymic)
#         {
#             // [1] Подготовка данных для тестирования
#
#             CreateClientRequest createClientRequest = new CreateClientRequest();
#             createClientRequest.Birthday = birthday;
#             createClientRequest.Document = document;
#             createClientRequest.SurName = surName;
#             createClientRequest.FirstName = firstName;
#             createClientRequest.Patronymic = patronymic;
#
#             _mockClientRepository.Setup(repository =>
#             repository.Create(It.IsNotNull<Client>())).Returns(1).Verifiable();
#
#             // [2] Исполнение тестируемого метода
#
#             var operationResult = _clientController.Create(createClientRequest);
#
#             // [3] Подготовка эталонного результата, проверка результата
#             Assert.IsType<OkObjectResult>(operationResult.Result);
#             var okObjectResult = (OkObjectResult)operationResult.Result;
#
#             _mockClientRepository.Verify(repository =>
#             repository.Create(It.IsNotNull<Client>()), Times.Never());
#         }
#
#     }
# }
