import Link from 'next/link';
import React from 'react';
import { AiFillGithub, AiFillTwitterCircle, AiFillLinkedin } from 'react-icons/ai';
import { DiCssdeck } from 'react-icons/di';

import { Span, Container, Div1, Div2, Div3, NavLink, SocialIcons } from './HeaderStyles';

const Header = () =>  (
    <Container>
        
        <Div1>
            <Link href="/">
                <a style={{ display: "flex", alignItems: "center", color: "white", marginBottom: "20px" }}>
                    <DiCssdeck size="3rem"/>  <Span>Justin Angeles</Span>
                </a>
            </Link>
        </Div1>
        
        <Div2>
        <li>
            <Link  href="#projects">
                <NavLink>Projects</NavLink>
            </Link>
        </li>
        
        <li>
            <Link href="#tech">
                <NavLink>Technologies</NavLink>
            </Link>
        </li>
        <li>
            <Link href="#contact">
                <NavLink>Contact</NavLink>
            </Link>
        </li>
        </Div2>
        
        <Div3>

            <SocialIcons target="_blank" href="https://github.com/justinsgithub">
                <AiFillGithub size="3rem" />
            </SocialIcons>
        
            <SocialIcons target="_blank" href="https://www.linkedin.com/in/justinaawd/">
                <AiFillLinkedin size="3rem" />
            </SocialIcons>
        
            <SocialIcons target="_blank" href="https://twitter.com/LoveJustinTyler">
                <AiFillTwitterCircle size="3rem" />                
            </SocialIcons>
        
        </Div3>

    </Container>
);

export default Header;
