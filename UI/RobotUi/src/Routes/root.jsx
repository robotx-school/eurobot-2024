import { Layout, Menu, theme, ConfigProvider } from 'antd';
import { Link, Outlet, useLocation } from 'react-router-dom';
import '../App.css';
import { routes } from './routes';


const { Content, Sider } = Layout;


export const Root = () => {
  let color_theme = "light";
  const location = useLocation();

  return (
    <ConfigProvider
      theme={{
        algorithm: theme.darkAlgorithm ? color_theme === "dark" : color_theme.defaultSelectedKeys
      }}
    >
      <Layout style={{
        marginLeft: 200,
      }}
      >
        <Sider
          className="main-slider"
          breakpoint="lg"
          style={{
            overflow: 'auto',
            height: '100vh',
            position: 'fixed',
            left: 0,
            top: 0,
            bottom: 0,
          }}
        >
          <div className="logo" />
          <Menu
            theme="dark"
            mode="inline"
            defaultSelectedKeys={[location.pathname.slice(1)]}
            items={routes.map(route => {
              return {
                key: route.path,
                icon: route.icon,
                label: <Link to={route.path}>{route.label}</Link>,
              }
            })}
          />
        </Sider>
        <Layout>
          <Content
            style={{
              margin: '24px 16px 0',
              overflow: 'initial',
            }}
          >
            <div
              style={{
                padding: 24,
                minHeight: 360,
                backgroundColor: "#fff" ? color_theme === "dark" : "#000",
              }}
            >
              <Outlet />
            </div>
          </Content>
        </Layout>
      </Layout>
    </ConfigProvider>
  );
};
