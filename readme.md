# servic.cpp：std::coroutine与asio的无缝衔接

Appweb的续作，基于C++20的`coroutine`与`boost::asio`的服务端。

路由器是另一个小组件：[yauntyour/router: 原生C++实现的路由器：Router](https://github.com/yauntyour/router)

# Example

```c++
#include "server.hpp"
#include <boost/asio.hpp>
#include <boost/asio/co_spawn.hpp>
#include <boost/asio/detached.hpp>
#include <boost/asio/use_awaitable.hpp>
namespace asio = boost::asio;
int main()
{
    try
    {
        rt::router ros;
        asio::io_context io_context;
        servic::Server server(io_context, 8080, 300000);

        ros.on("/", [](std::string &input, std::string &output)
               {
            output = "HTTP/1.1 200 OK\r\n\r\nHello World!";
            return 0; });
        ros.on("/test", [](std::string &input, std::string &output)
               {
            output = "HTTP/1.1 200 OK\r\n\r\nHello World!";
            return 0; });

        server.run(ros);
    }
    catch (std::exception &e)
    {
        std::cerr << "Exception: " << e.what() << "\n";
        return 1;
    }
    return 0;
}
```

