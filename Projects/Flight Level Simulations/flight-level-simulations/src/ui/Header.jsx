import styled from 'styled-components'

import {IoAirplane} from 'react-icons/io5'

const StyledHeader = styled.header`
    background-color: var(--color-black-100);
    padding: 10px 20px;
`

const StyledH1 = styled.h1`
    color: var(--color-grey-0);
    font-size: 36px;
`

const Icon = styled.span`
    vertical-align: middle;
    margin-left: 5px;
`

const Header = () => {
    return (
        <StyledHeader>
            <StyledH1>Flight Level Simulations<Icon><IoAirplane /></Icon></StyledH1>
        </StyledHeader>
    )
}

export default Header