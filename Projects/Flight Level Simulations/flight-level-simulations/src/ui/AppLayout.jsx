import { Outlet } from 'react-router-dom';
import styled from 'styled-components';
import Header from './Header';
import Sidebar from './Sidebar';

const StyledAppLayout = styled.div`
`

const Main = styled.main`
    background-color: var(--color-raisin-black-100);
    padding: 10px 20px;
`

const Container = styled.div`
`

const AppLayout = () => {
    return (
        <StyledAppLayout>
            <Header />
            <Sidebar />
            <Main>
                <Container>
                    <Outlet />
                </Container>
            </Main>
        </StyledAppLayout>
    )
}

export default AppLayout