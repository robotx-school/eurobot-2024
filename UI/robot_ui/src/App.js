import { BellOutlined, CodeOutlined, ControlOutlined } from '@ant-design/icons';
import { Layout, Menu, theme } from 'antd';
import React from 'react';
import './App.css';

const { Content, Sider } = Layout;

const App = () => {
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  const menu = [
    {
      key: '0',
      icon: <BellOutlined />,
      label: "Intro"
    },
    {
      key: '1',
      icon: <ControlOutlined />,
      label: "Joystick"
    },
    {
      key: '2',
      icon: <CodeOutlined />,
      label: "SPI Terminal"
    }
  ];
  return (
    <Layout>
      <Sider
        className="main-slider"
        breakpoint="lg"
        collapsedWidth="0"
        style={{
          height: '100vh',
        }}

      >
        <div className="logo" />
        <Menu
          theme="dark"
          mode="inline"
          defaultSelectedKeys={['0']}
          items={menu}
        />
      </Sider>
      <Layout>

        <Content
          style={{
            margin: '24px 16px 0',
          }}
        >
          <div
            style={{
              padding: 24,
              minHeight: 360,
              background: colorBgContainer,
            }}
          >
            Content
          </div>
        </Content>

      </Layout>
    </Layout>
  );
};
export default App;