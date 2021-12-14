//@author Jared Scott ☯
//Built from an example found here: https://www.npmjs.com/package/react-pdf

import React, { useState } from "react";
import { Document, Page } from "react-pdf";

export default function PDFViewer(props) {
  const [numPages, setNumPages] = useState(null);
  const [pageNumber, setPageNumber] = useState(1); //setting 1 to show first page

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
    setPageNumber(1);
  }

  function changePage(offset) {
    setPageNumber(prevPageNumber => prevPageNumber + offset);
  }

  function previousPage() {
    changePage(-1);
  }

  function nextPage() {
    changePage(1);
  }

  const { pdf } = props;

  return (
    <div>
		<div>
			<button type="button" disabled={pageNumber <= 1} onClick={previousPage}>
			  Previous
			</button>
			<button
			  type="button"
			  disabled={pageNumber >= numPages}
			  onClick={nextPage}
			>
			  Next
			</button>
			<span style={{padding:"20px", 'font-size':"20px"}}>
			  Page {pageNumber || (numPages ? 1 : "--")} of {numPages || "--"}
			</span>
		</div>
		<Document
			file={pdf}
			options={{ workerSrc: "/pdf.worker.js" }}
			onLoadSuccess={onDocumentLoadSuccess}
			>
			<Page pageNumber={pageNumber} />
		</Document>
    </div>
  );
}