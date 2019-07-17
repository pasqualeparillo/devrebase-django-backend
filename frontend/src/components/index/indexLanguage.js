import React, { useContext } from "react";
import { FetchContext } from "../../store/fetch";
import axios from "axios";
import Aws from "../../images/icons/aws.png";
import Ruby from "../../images/icons/ruby.png";
import Java from "../../images/icons/java.png";
import Javascript from "../../images/icons/javascript.png";
import Csharp from "../../images/icons/csharp.png";
import ReactIcon from "../../images/icons/react.png";
import Python from "../../images/icons/python.png";
import Sql from "../../images/icons/sql.png";
import { Container } from "../shared/container";
import { TextPrimary, TextSub } from "../shared/text";

export function IndexLanguage() {
  return (
    <Container>
      <div className="flex flex-col lg:w-5/6 w-11/12 items-start justify-center mx-auto">
        <p className="lg:pl-2 pt-6 pb-6 font-semibold">Popular Skills</p>
        <div className="w-full flex justify-around flex-wrap mx-auto">
          {languages.map((language, id) => (
            <LanguageCard
              languageIcon={language.languageIcon}
              language={language.language}
              key={id}
              bgColor={language.bgColor}
            />
          ))}
        </div>
      </div>
    </Container>
  );
}

export function LanguageCard(props) {
  const { setJobs } = useContext(FetchContext);
  async function handleClick() {
    await axios
      .get(`http://127.0.0.1:8000/?search=${props.language}`)
      .then(response => setJobs({ jobs: response.data }))
      .catch(error => {
        console.log(error);
      });
  }
  return (
      <div
        className="lg:w-1/6 md:w-2/5 w-2/5 flex flex-grow rounded lg:p-6 p-4 lg:flex-1 sm:mt-2 mr-2 cursor-pointer card card-shadow transform relative "
        onClick={handleClick}
      >
        <div className="w-1/2 flex justify-start items-center content-center relative h-full">
          <img className="absolute " src={props.languageIcon} />
        </div>
        <div className="flex flex-wrap flex-grow lg:text-right md:text-left text-right items-start">
          <div className="w-full">
            <TextPrimary>
              {props.language}
            </TextPrimary>
          </div>
          <div className="w-full">
           <TextSub>1234 Jobs</TextSub>
          </div>
        </div>
      </div>
  );
}

const languages = [
  {
    id: 0,
    languageIcon: Java,
    language: "Java",
    bgColor: "bg-blue-600-lighter"
  },
  {
    id: 1,
    languageIcon: Javascript,
    language: "Javascript",
    bgColor: "bg-yellow-light"
  },
  {
    id: 2,
    languageIcon: Sql,
    language: "SQL",
    bgColor: "bg-blue-600"
  },
  {
    id: 3,
    languageIcon: Aws,
    language: "AWS",
    bgColor: "bg-orange"
  },
  {
    id: 4,
    languageIcon: Python,
    language: "Python",
    bgColor: "bg-blue-600-dark"
  },
  {
    id: 5,
    languageIcon: ReactIcon,
    language: "React",
    bgColor: "bg-blue-600"
  },
  {
    id: 6,
    languageIcon: Ruby,
    language: "Ruby",
    bgColor: "bg-red-light"
  },
  {
    id: 7,
    languageIcon: Csharp,
    language: "Csharp",
    bgColor: "bg-blue-600"
  }
];
